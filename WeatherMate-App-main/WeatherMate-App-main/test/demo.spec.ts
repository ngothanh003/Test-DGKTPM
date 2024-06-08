import { test, expect } from '@playwright/test';

test('test index.html', async ({ page }) => {
  await page.goto('/index.html');  // Use relative URL

  // Example assertion
  await expect(page).toHaveTitle('Your Page Title');
});