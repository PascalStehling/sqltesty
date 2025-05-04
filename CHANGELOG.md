# CHANGELOG


## v0.2.0 (2025-05-04)

### Features

- :sparkles: add new dtype difference output
  ([`c72a521`](https://github.com/PascalStehling/sqltesty/commit/c72a521ddf9d0192b1e32543fd22f111b2ce284b))

- :sparkles: improve sorted row handling
  ([`5be4269`](https://github.com/PascalStehling/sqltesty/commit/5be426937ba6308f49eec32289c2dbad3385b314))

The problem was that with order by you get an ordering, but without the order can be random. So now
  depending if the row is sorted or not it will be compared as it is or it will be sorted by the
  test, to make sure the values are allways in the same order

### Refactoring

- :recycle: move functions for better structure
  ([`19afe27`](https://github.com/PascalStehling/sqltesty/commit/19afe271bbbf9c6c0d23263c4effe18f8b139e1d))

- :rotating_light: add and fix linter stuff
  ([`f8c9f38`](https://github.com/PascalStehling/sqltesty/commit/f8c9f38853c925d1d0be17c248523e9e6b964352))

improve the linter and check everything


## v0.1.4 (2025-05-03)

### Bug Fixes

- :green_heart: another try of fixing pypi publishing
  ([`e2b6b3c`](https://github.com/PascalStehling/sqltesty/commit/e2b6b3ca9a18c7a752cad724c596ed52dedd77e8))

github actions debugging is the worst :(


## v0.1.3 (2025-05-03)

### Bug Fixes

- :green_heart: fix pypi upload
  ([`151a341`](https://github.com/PascalStehling/sqltesty/commit/151a341fa1bc22fe6bf5acfbffd2669a51a2c92f))


## v0.1.2 (2025-05-03)

### Bug Fixes

- :bug: some more ci stuff
  ([`8209ee9`](https://github.com/PascalStehling/sqltesty/commit/8209ee974de37b366124dc340a1e96682d9609cf))


## v0.1.1 (2025-04-29)

### Bug Fixes

- :bug: fix project name
  ([`13e6ddc`](https://github.com/PascalStehling/sqltesty/commit/13e6ddc6067a27840a069511614402a279ab4de4))


## v0.1.0 (2025-04-29)

### Features

- :tada: Initial commit
  ([`edd87cd`](https://github.com/PascalStehling/sqltesty/commit/edd87cdbcabe7d5a985373aeac485c849ab13f73))

basic steup stuff
