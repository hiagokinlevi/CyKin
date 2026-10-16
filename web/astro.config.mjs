import { defineConfig } from 'astro/config';
import react from '@astrojs/react';

export default defineConfig({
  site: 'https://opencyber.academy',
  output: 'static',
  build: { format: 'directory' },
  integrations: [react()],
});
