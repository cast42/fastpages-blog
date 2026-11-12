# Active Support 8 requires Ruby 3.2 or newer.
FROM ruby:3.3

RUN apt-get update && apt-get install -y --no-install-recommends nodejs \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /data
COPY Gemfile Gemfile.lock ./
RUN bundle install
