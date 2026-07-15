                        +----------------+
                        |      User      |
                        +----------------+
                        | id             |
                        | username       |
                        | email          |
                        | password_hash  |
                        | created_at     |
                        +--------+-------+
                                 |
                                 |
                                 | 1
                                 |
                                 | N
                  +--------------v---------------+
                  |       CollectionItem         |
                  +------------------------------+
                  | id                           |
                  | user_id (FK)                 |
                  | card_id (FK)                 |
                  | quantity                     |
                  | condition                    |
                  | purchase_price               |
                  | purchase_date                |
                  | acquisition_method           |
                  | created_at                   |
                  +--------------+---------------+
                                 |
                                 |
                                 |
                                 |
                  +--------------v---------------+
                  |            Card              |
                  +------------------------------+
                  | id                           |
                  | pokemon_api_id               |
                  | set_id (FK)                  |
                  | name                         |
                  | number                       |
                  | rarity                       |
                  | type                         |
                  | hp                           |
                  | image_url                    |
                  +--------------+---------------+
                                 |
               +-----------------+-----------------+
               |                                   |
               |                                   |
               |                                   |
      +--------v--------+               +----------v-----------+
      |      Set        |               |    PriceHistory      |
      +-----------------+               +----------------------+
      | id              |               | id                   |
      | api_set_id      |               | card_id (FK)         |
      | name            |               | market_price         |
      | series          |               | updated_at           |
      | release_date    |               +----------------------+
      +-----------------+