import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://opencyber.academy',
  output: 'static',
  build: { format: 'directory' },
});
