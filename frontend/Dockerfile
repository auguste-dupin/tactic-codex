FROM node:20-alpine
WORKDIR /app
COPY package.json vite.config.js tailwind.config.js index.html ./
COPY src ./src
RUN npm install && npx tailwindcss -i ./src/index.css -o ./src/output.css --minify || true
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
