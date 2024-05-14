const { test, expect } = require('@playwright/test')


test('Home Page', async ({ page }) => { // page is called a feature

    await page.goto('https://www.demoblaze.com/index.html')

    const pageTitle = await page.title();
    console.log(`page tile is: ${pageTitle}`);

    await expect(page).toHaveTitle('STORE');

    const pageURL = await page.url()

    console.log(`page URL: ${pageURL}`)

    await expect(page).toHaveURL('https://www.demoblaze.com/index.html')

    await page.close()

}) // this is called a test block
