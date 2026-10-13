import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://cykin.org',
  output: 'static',
  build: { format: 'directory' },
});
