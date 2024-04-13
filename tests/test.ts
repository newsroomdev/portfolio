import { expect, test } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright'; // 1

test('index page has expected h1', async ({ page }) => {
	await page.goto('/');
	await expect(page.getByRole('heading', { name: 'Gerald Rich' })).toBeVisible();
});

test.skip('homepage', () => {
	test('should not have any automatically detectable accessibility issues', async ({ page }) => {
		await page.goto('/');

		const accessibilityScanResults = await new AxeBuilder({ page }).analyze();

		expect(accessibilityScanResults.violations).toEqual([]);
	});
});
