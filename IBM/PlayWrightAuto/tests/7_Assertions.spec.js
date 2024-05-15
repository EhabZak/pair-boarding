const {test,expect} = require ('@playwright/test')

test ('Assertions', async({page})=>{

    await page.goto('https://demo.nopcommerce.com/register')
    //! 1- expect (page).toHaveURL()  //Page has URL
    await expect(page).toHaveURL('https://demo.nopcommerce.com/register')
    //! 2- expect (page).toHaveTitle() //Page has title
    await expect(page).toHaveTitle('nopCommerce demo store. Register')
    //! 3- expect (locator).toBeVisible()  // Element is visible
    const logoElement = await page.locator(".header-logo")
    await expect(logoElement).toBeVisible()
    //! 4- expect (locator).toBeEnabled() // Element is visible / Control is enabled
    const search = await page.locator('#small-searchterms')
    await expect(search).toBeEnabled()

    //! 5- expect (locator).toBeChecked() //Radio/Checkbox is checked
    const male = await page.locator('#gender-male')
    //select the radio button
    await male.click()
    await expect(male).toBeChecked()

    const checkbox = await page.locator('#Newsletter')
    await expect(checkbox).toBeChecked()

    //! 6- expect (locator).toHaveAttribute()  //Element has attribute
    const register = await page.locator('#register-button')
    await expect(register).toHaveAttribute('type','submit')

    //! 7- expect (locator), toHaveText() // Element matches text // exact text match
    await expect(await page.locator('.page-title h1')).toHaveText('Register') //full text check
    //! 8- expect(locator), toContainText() // Element contains text // partial text match
    await expect(await page.locator('.page-title h1')).toContainText ('Reg') // checks partial text

    //! 9- expect(locator), toHaveValue(value) //Input has a value
    const email = await page.locator('#Email')
    await email.fill('test@demo.com')
    await expect(email).toHaveValue('test@demo.com')

    //! 10- expect (Locator), toHaveCount() //List of Element has a given length
    const options = await page.locator("select[name='DateOfBirthMonth'] option ")

    await expect(options).toHaveCount(13) // very useful you can have count for all images on a web page


    await page.close()

})
