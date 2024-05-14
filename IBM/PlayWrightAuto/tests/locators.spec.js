import {test,expect} from '@playwright/test'

test ('Locators', async ({page})=>{

await page.goto('https://www.demoblaze.com/index.html')

// click on log in button - using property selector

// await page.locator('id=login2').click()
await page.click('id=login2')

// provide user name - using CSS

// await page.locator('#loginusername').fill('pavanol')
// await page.type('#loginusername','pavanol')
await page.fill('#loginusername','pavanol')

//provide password - also using CSS

await page.fill("input[id='loginpassword']",'test@123')

// click on log in button - used xpath to locate the element

await page.click("//button[normalize-space()='Log in']")

// find the logout button - used xpath to locate the element

const LogoutLink = await page.locator("//a[@id='logout2']")

await expect(LogoutLink).toBeVisible()

await page.close()

})
