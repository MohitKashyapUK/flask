version: '3.7'

services:
  telegram-bot-api:
    image: aiogram/telegram-bot-api:latest
    environment:
      TELEGRAM_API_ID: "27269597"
      TELEGRAM_API_HASH: "ef91ab7dfb77baea3d5f87e5d6cd5744"
    volumes:
      - telegram-bot-api-data:/var/lib/telegram-bot-api
    ports:
      - 8081:8081

volumes:
  telegram-bot-api-data:
