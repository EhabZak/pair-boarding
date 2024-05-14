// import { test, expect } from '@playwright/test'
const { test, expect } = require('@playwright/test')


test('locateMultipleElements', async ({ page }) => {

    await page.goto('https://www.demoblaze.com/index.html')

//     // 1-find all a elements in the page

//     //    const links = await page.$$('a')

//     //    for (const link of links) {

//     //        const linkText = await link.textContent()
//     //        console.log(linkText)

//     //     }
//     // 2-find the name of the product on the first page

    // await page.waitForSelector('.hrefch');
    await page.waitForSelector('#tbodyid h4 a');

    // using property selector
    // const products = await page.$$('.hrefch')
    //using CSS
    const products = await page.$$("#tbodyid h4 a")

    for (const product of products) {
        const productName = await product.textContent()
        console.log(productName)
    }
})

//!/ using xpath


// test('locateMultipleElements', async ({ page }) => {

//     await page.goto('https://www.demoblaze.com/index.html')

//     // 1-find all a elements in the page

//     //    const links = await page.$$('a')

//     //    for (const link of links) {

//     //        const linkText = await link.textContent()
//     //        console.log(linkText)

//     //     }

//     // 2-locate all products displayed on homepage

//     await page.waitForSelector("//div[@id='tbodyid']//h4//a")

//     const products = await page.$$("//div[@id='tbodyid']//h4//a")

//     for (const product of products) {
//         const productName = await product.textContent()
//         console.log(productName)
//     }

// })
