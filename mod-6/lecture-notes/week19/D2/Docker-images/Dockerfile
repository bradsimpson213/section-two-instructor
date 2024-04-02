FROM node:15-alpine3.10
EXPOSE 3000
WORKDIR /app
COPY package*.json ./
# COPY package.json /app
# COPY package-lock.json /app
RUN npm install
COPY . .
CMD ["npm", "start"]

