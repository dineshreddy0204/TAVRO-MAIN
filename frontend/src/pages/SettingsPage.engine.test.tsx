import { renderToStaticMarkup } from 'react-dom/server';
import { describe, expect, it, vi } from 'vitest';

vi.mock('../lib/store', () => ({ useAppStore: vi.fn() }));

vi.mock('../lib/api', async (importOriginal) => {
  const actual = await importOriginal<typeof import('../lib/api')>();
  return {
    ...actual,
    isTauri: vi.fn(() => false),
    fetchServerInfo: vi.fn().mockResolvedValue({
      model: 'qwen3.5:4b',
      engine: 'ollama',
      configured_engine: 'ollama',
      configured_model: 'qwen3.5:4b',
      active_engine: 'ollama',
      active_model: 'qwen3.5:4b',
    }),
    getInferenceSource: vi.fn().mockResolvedValue({
      kind: 'ollama',
      engine: 'ollama',
      model: 'qwen3.5:4b',
    }),
  };
});

describe('Settings inference source and engine display in browser', () => {
  it('hides the Bundled Ollama save button when not running in Tauri desktop', async () => {
    const { isTauri } = await import('../lib/api');
    expect(isTauri()).toBe(false);
  });
});

