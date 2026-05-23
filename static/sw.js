const CACHE = 'sitbell-v1';
const STATIC = ['/', '/static/manifest.json'];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE).then(c => c.addAll(STATIC)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  // Sound files: network first, no cache (dynamic folder)
  if (e.request.url.includes('/sounds/') || e.request.url.includes('/api/')) {
    e.respondWith(fetch(e.request).catch(() => new Response('{}', {headers: {'Content-Type': 'application/json'}})));
    return;
  }
  // Everything else: cache first
  e.respondWith(
    caches.match(e.request).then(cached => cached || fetch(e.request).then(resp => {
      const clone = resp.clone();
      caches.open(CACHE).then(c => c.put(e.request, clone));
      return resp;
    }))
  );
});
