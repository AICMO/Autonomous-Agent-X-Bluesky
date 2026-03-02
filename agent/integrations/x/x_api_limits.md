# X API v2 Rate Limits

Source: X Developer Portal, 2026-03-02

## Tweets

| Endpoint | Pro | Basic |
|----------|-----|-------|
| POST /2/tweets | 100 req / 24h per user | 100 req / 24h per user |
| DELETE /2/tweets/:id | 50 req / 15min per user | 100 req / 15min per user |
| GET /2/tweets | 900 req / 15min per app | 15 req / 15min per app |
| GET /2/tweets/:id | 900 req / 15min per app | 15 req / 15min per app |
| GET /2/tweets/:id/liking_users | 75 req / 15min | 5 req / 15min |
| GET /2/tweets/:id/quote_tweets | 75 req / 15min per app | 5 req / 15min per app |
| GET /2/tweets/:id/retweeted_by | 75 req / 15min per app | 5 req / 15min per app |
| GET /2/tweets/:id/retweets | 75 req / 15min per app | 10 req / 15min per app |
| GET /2/tweets/counts/all | 300 req / 15min per app | 5 req / 15min per app |
| GET /2/tweets/counts/recent | 300 req / 15min per app | 5 req / 15min per app |
| GET /2/tweets/search/all | 300 req / 15min per app, 1/sec | 60 req / 15min per user |
| GET /2/tweets/search/recent | 450 req / 15min per app | 60 req / 15min per app |
| GET /2/tweets/search/stream | 450 req / 15min per app | - |
| GET /2/tweets/search/stream/rules | 450 req / 15min per app | - |
| POST /2/tweets/search/stream/rules | 1000 req / 15min per app | 200 req / 15min per app |
| PUT /2/tweets/:tweet_id/hidden | 50 req / 15min per user | 5 req / 15min per user |

## Likes

| Endpoint | Pro | Basic |
|----------|-----|-------|
| POST /2/users/:id/likes | 50 req / 24h per user | 5 req / 24h per user |
| DELETE /2/users/:id/likes/:tweet_id | 50 req / 15min per user | 5 req / 24h per user |
| GET /2/users/:id/liked_tweets | 75 req / 15min per user | 5 req / 15min per user |

## Retweets

| Endpoint | Pro | Basic |
|----------|-----|-------|
| POST /2/users/:id/retweets | 50 req / 15min per user | 5 req / 15min per user |
| DELETE /2/users/:id/retweets/:tweet_id | 900 req / 15min per user | 15 req / 15min per user |

## Users

| Endpoint | Pro | Basic |
|----------|-----|-------|
| GET /2/users | 900 req / 15min | 100 req / 24h |
| GET /2/users/:id | 300 req / 15min per app | 500 req / 24h per app |
| GET /2/users/by | 300 req / 15min per app | 500 req / 24h per app |
| GET /2/users/by/username/:username | 900 req / 15min | 100 req / 24h |
| GET /2/users/me | 900 req / 15min per user | - / 24h per user |
| GET /2/users/search | 300 req / 15min per app | 5 req / 15min per app |
| GET /2/users/:id/mentions | 450 req / 15min per app | 15 req / 15min per app |
| GET /2/users/:id/tweets | 1500 req / 15min per app | 10 req / 15min per app |
| GET /2/users/by/username/:username/mentions | 450 req / 15min per app | 25 req / 15min per app |
| GET /2/users/by/username/:username/tweets | 900 req / 15min per user | 5 req / 15min per user |
| GET /2/users/:id/timelines/reverse_chronological | 900 req / 15min per user | 5 req / 15min per user |

## Following / Blocking / Muting

| Endpoint | Pro | Basic |
|----------|-----|-------|
| POST /2/users/:id/following | 50 req / 15min per user | 5 req / 15min per user |
| DELETE /2/users/:source_user_id/following/:target_user_id | 50 req / 15min per user | 5 req / 15min per user |
| POST /2/users/:id/muting | 50 req / 15min per user | 5 req / 15min per user |
| DELETE /2/users/:source_user_id/muting/:target_user_id | 50 req / 15min per user | 5 req / 15min per user |
| GET /2/users/:id/blocking | 15 req / 15min per user | 100 req / 15min per user |
| GET /2/users/:id/muting | 900 req / 15min per user | 100 req / 24h per user |

## Direct Messages

| Endpoint | Pro | Basic |
|----------|-----|-------|
| POST /2/dm_conversations | 1440 req / 24h per app | 1 req / 24h per app |
| POST /2/dm_conversations/:id/message | 1440 req / 24h per app | 1 req / 24h per app |
| POST /2/dm_conversations/with/:participant_id/messages | 1440 req / 24h per app | 1 req / 24h per app |
| DELETE /2/dm_events/:id | 4000 req / 24h per app | 2500 req / 24h per app |
| GET /2/dm_conversations/:id/dm_events | 15 req / 15min per user | 1 req / 24h per user |
| GET /2/dm_conversations/with/:participant_id/dm_events | 15 req / 15min per user | 1 req / 24h per user |
| GET /2/dm_events | 15 req / 15min per user | 1 req / 24h per user |
| GET /2/dm_events/:id | 15 req / 15min | 5 req / 24h |

## Lists

| Endpoint | Pro | Basic |
|----------|-----|-------|
| POST /2/lists | 300 req / 15min per user | 5 req / 24h per user |
| DELETE /2/lists/:id | 300 req / 15min per user | 5 req / 15min per user |
| PUT /2/lists/:id | 300 req / 15min per user | 5 req / 15min per user |
| POST /2/lists/:id/members | 300 req / 15min | 5 req / 15min |
| DELETE /2/lists/:id/members/:user_id | 300 req / 15min | 5 req / 15min |
| GET /2/lists/:id | 75 req / 15min per user | 5 req / 15min per user |
| GET /2/lists/:id/members | 900 req / 15min per app | 25 req / 15min per app |
| GET /2/lists/:id/tweets | 900 req / 15min per user | 5 req / 15min per user |
| GET /2/users/:id/list_memberships | 75 req / 15min per app | 25 req / 15min per app |
| GET /2/users/:id/owned_lists | 15 req / 15min per app | 500 req / 24h per app |
| GET /2/users/:id/pinned_lists | 15 req / 15min per app | 500 req / 24h per app |
| POST /2/users/:id/followed_lists | 50 req / 15min per user | 5 req / 15min per user |
| DELETE /2/users/:id/followed_lists/:list_id | 50 req / 15min per user | 5 req / 15min per user |
| POST /2/users/:id/pinned_lists | 50 req / 15min per user | 5 req / 15min per user |
| DELETE /2/users/:id/pinned_lists/:list_id | 75 req / 15min per user | 5 req / 15min per user |

## Bookmarks

| Endpoint | Pro | Basic |
|----------|-----|-------|
| POST /2/users/:id/bookmarks | 50 req / 15min per user | 5 req / 15min per user |
| DELETE /2/users/:id/bookmarks/:tweet_id | 50 req / 15min per user | 5 req / 15min per user |
| GET /2/users/:id/bookmarks | 180 req / 15min per user | 10 req / 15min per user |
| GET /2/users/:id/bookmarks/folders | 50 req / 15min per app | 5 req / 15min per app |
| GET /2/users/:id/bookmarks/folders/:folder_id | 50 req / 15min per app | 5 req / 15min per app |

## Spaces

| Endpoint | Pro | Basic |
|----------|-----|-------|
| GET /2/spaces | 300 req / 15min per app | 25 req / 15min per app |
| GET /2/spaces/:id | 300 req / 15min per app | 25 req / 15min per app |
| GET /2/spaces/:id/buyers | 300 req / 15min per app | 25 req / 15min per app |
| GET /2/spaces/:id/tweets | 300 req / 15min per app | 25 req / 15min per app |
| GET /2/spaces/by/creator_ids | 1 req / sec per app | 25 req / sec per app |
| GET /2/spaces/search | 300 req / 15min per app | 25 req / 15min per app |

## Communities

| Endpoint | Pro | Basic |
|----------|-----|-------|
| GET /2/communities/:id | 300 req / 15min per user | 1 req / 15min per user |
| GET /2/communities/search | 300 req / 15min per app | 25 req / 15min per app |

## Trends

| Endpoint | Pro | Basic |
|----------|-----|-------|
| GET /2/trends/by/woeid/:id | 10 req / 15min per user | 1 req / 15min per user |
| GET /2/users/personalized_trends | 200 req / 15min per user | 20 req / 15min per user |

## Media

| Endpoint | Pro | Basic |
|----------|-----|-------|
| POST /2/media/upload | 50000 req / 24h per app | 8335 req / 24h per app |
| POST /2/media/upload/:id/append | 180000 req / 24h per app | 180000 req / 24h per app |
| POST /2/media/upload/:id/finalize | 180000 req / 24h per app | 180000 req / 24h per app |
| POST /2/media/upload/initialize | 180000 req / 24h per app | 180000 req / 24h per app |
| GET /2/media/upload | 100000 req / 24h per app | 16670 req / 24h per app |
| POST /2/media/metadata | 500 req / 15min per user | 500 req / 24h per user |
| POST /2/media/metadata/create | 50000 req / 24h per app | 8335 req / 24h per app |
| POST /2/media/subtitles | 10000 req / 24h per app | 1667 req / 24h per app |
| DELETE /2/media/subtitles | 10000 req / 24h per app | 1667 req / 24h per app |

## Compliance

| Endpoint | Pro | Basic |
|----------|-----|-------|
| GET /2/compliance/jobs | 150 req / 15min per app | 5 req / 15min per app |
| GET /2/compliance/jobs/:job_id | 150 req / 15min per app | 5 req / 15min per app |
| POST /2/compliance/jobs | 150 req / 15min per app | 15 req / 15min per app |

## Usage

| Endpoint | Pro | Basic |
|----------|-----|-------|
| GET /2/usage/tweets | 50 req / 15min per app | 50 req / 15min per app |

## News

| Endpoint | Pro | Basic |
|----------|-----|-------|
| GET /2/news/:id | 50 req / 15min per user | 5 req / 15min per user |
| GET /2/news/search | 50 req / 15min per app | 5 req / 15min per app |