const CACHE_NAME = 'pokemon-pinyin-v2';
const urlsToCache = [
  './',
  './index.html',
  './manifest.json',
  './pokemon_database.js'
];

// 安装 Service Worker
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

// 激活 Service Worker
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CACHE_NAME) {
            console.log('Deleting old cache:', cacheName);
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
});

// 拦截网络请求
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);

  // 判断是否是宝可梦图片请求
  const isPokemonImage = url.pathname.includes('/images/pokemon/');

  event.respondWith(
    caches.match(event.request)
      .then(response => {
        // 缓存命中，返回缓存的资源
        if (response) {
          return response;
        }

        // 否则发起网络请求
        return fetch(event.request).then(
          response => {
            // 检查是否是有效响应
            if (!response || response.status !== 200) {
              return response;
            }

            // 克隆响应
            const responseToCache = response.clone();

            // 缓存新资源（特别是宝可梦图片）
            if (isPokemonImage || response.type === 'basic') {
              caches.open(CACHE_NAME)
                .then(cache => {
                  cache.put(event.request, responseToCache);
                });
            }

            return response;
          }
        ).catch(() => {
          // 如果网络请求失败，对于图片可以返回一个占位符
          // 这里简单返回失败，实际应用中可以返回默认图片
          return new Response('Network error', {
            status: 408,
            headers: { 'Content-Type': 'text/plain' }
          });
        });
      })
  );
});
