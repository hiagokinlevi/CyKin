import { siteLanguage } from './i18n';
import { dashboardCopy } from './student-dashboard';

type KeyInfo = { id: string; label: string; token_prefix: string; created_at: number; expires_at: number;
  last_used_at: number | null; use_count: number; revoked_at: number | null };

export function initializeStudentMcpKeys(): { load: () => Promise<void>; clear: () => void } {
  const language = siteLanguage();
  const t = dashboardCopy[language];
  const form = document.getElementById('ai-key-form') as HTMLFormElement;
  const label = document.getElementById('ai-key-label') as HTMLInputElement;
  label.placeholder = t.keyPlaceholder;
  const list = document.getElementById('ai-key-list')!;
  const message = document.getElementById('ai-key-message')!;
  const oneTime = document.getElementById('ai-key-once')!;
  const secret = document.getElementById('ai-key-secret')!;
  const copyButton = document.getElementById('ai-key-copy') as HTMLButtonElement;
  const dismissButton = document.getElementById('ai-key-dismiss') as HTMLButtonElement;
  const date = (timestamp: number | null) => timestamp
    ? new Intl.DateTimeFormat({ en: 'en-US', pt: 'pt-BR', es: 'es-ES' }[language], { dateStyle: 'medium' }).format(timestamp * 1000)
    : '—';
  const hideSecret = () => { secret.textContent = ''; oneTime.hidden = true; };

  async function load(): Promise<void> {
    const response = await fetch('/auth/mcp-keys', { credentials: 'same-origin', cache: 'no-store' });
    if (!response.ok) { message.textContent = t.keyError; return; }
    const data = await response.json() as { keys: KeyInfo[] };
    list.replaceChildren();
    if (!data.keys.length) { const note = document.createElement('p'); note.className = 'empty-note'; note.textContent = t.noKeys; list.append(note); }
    for (const item of data.keys) {
      const row = document.createElement('div'); row.className = 'key-row';
      const info = document.createElement('div');
      const title = document.createElement('strong'); title.textContent = item.label;
      const details = document.createElement('small');
      const state = item.revoked_at ? t.keyRevokedLabel : item.expires_at <= Date.now() / 1000 ? t.keyExpired : t.keyActive;
      details.textContent = `${item.token_prefix}… · ${state} · ${item.use_count} ${t.keyUses} · ${t.keyLastUsed}: ${date(item.last_used_at)} · ${t.keyExpires}: ${date(item.expires_at)}`;
      info.append(title, details); row.append(info);
      if (!item.revoked_at && item.expires_at > Date.now() / 1000) {
        const revoke = document.createElement('button'); revoke.type = 'button'; revoke.textContent = t.revokeKey;
        revoke.addEventListener('click', async () => {
          revoke.disabled = true;
          try {
            const response = await fetch(`/auth/mcp-keys/${encodeURIComponent(item.id)}`, { method: 'DELETE', credentials: 'same-origin', cache: 'no-store' });
            if (!response.ok) throw new Error('revoke');
            message.textContent = t.keyRevoked; await load();
          } catch { message.textContent = t.keyError; revoke.disabled = false; }
        });
        row.append(revoke);
      }
      list.append(row);
    }
  }

  form.addEventListener('submit', async event => {
    event.preventDefault(); if (!form.reportValidity()) return;
    const button = form.querySelector<HTMLButtonElement>('button[type="submit"]')!;
    button.disabled = true; hideSecret(); message.textContent = '';
    try {
      const response = await fetch('/auth/mcp-keys', {
        method: 'POST', credentials: 'same-origin', cache: 'no-store', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ label: label.value.trim() }),
      });
      if (response.status === 409) throw new Error('limit');
      if (!response.ok) throw new Error('create');
      const created = await response.json() as { token: string };
      secret.textContent = created.token; oneTime.hidden = false;
      message.textContent = t.keyCreated; label.value = ''; await load();
    } catch (error) { message.textContent = error instanceof Error && error.message === 'limit' ? t.keyLimit : t.keyError; }
    finally { button.disabled = false; }
  });
  copyButton.addEventListener('click', async () => {
    if (!secret.textContent) return;
    try { await navigator.clipboard.writeText(secret.textContent); message.textContent = t.keyCopied; }
    catch { message.textContent = t.keyError; }
  });
  dismissButton.addEventListener('click', hideSecret);
  return { load, clear: () => { hideSecret(); list.replaceChildren(); message.textContent = ''; } };
}
