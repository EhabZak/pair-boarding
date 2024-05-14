/*

page.getByAltText() to locate an element, usually image, by its text alternative.
page.getByPlaceholder() to locate an input by placeholder.
page.getByRole() to locate by explicit and implicit accessibility attributes.(actionable elements like button)
page.getByText() to locate by text content.
page.getByLabel() to locate a form control by associated label's text.
       await page.getByLabel('Password').fill('secret');
page.getByTitle() to locate an element by its title attribute.
        await expect(page.getByTitle('Issues count')).toHaveText('25 issues');
page.getByTestId() to locate an element based on its data-testid attribute (other attributes can be configured).
       <button data-testid="directions">Itinéraire</button>
*/


import {test,expect} from '@playwright/test'


test ('Builtin-locators', async({page})=>{

    await page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    //1-page.getByAltText() to locate an element, usually image, by its text alternative.
    const  logo = await page.getByAltText('company-branding')

    await expect(logo).toBeVisible()

    // 2-page.getByPlaceholder() to locate an input by placeholder.
     await page.getByPlaceholder('Username').fill('Admin')
     await page.getByPlaceholder('password').fill('admin123')
     await page.getByRole('button', {type:'submit'}).click()
    //  await page.getByRole('button', {class:'oxd-button oxd-button--medium oxd-button--main orangehrm-login-button'}).click()

    // 3-page.getByText() to locate by text content.
    const name = await page.locator("//p[@class='oxd-userdropdown-name']").textContent()
    await expect( await page.getByText(name)).toBeVisible()

    await page.getByLabel('Password').fill('secret');

    await page.close()



})
