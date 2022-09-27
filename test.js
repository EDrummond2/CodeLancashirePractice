console.log("JS is working")

window.addEventListener('load', () => {
    console.log("Event Listener is working")
    let test_div = document.createElement('div')
    test_div.innerHTML = "<h1>The JS is working<h1>"
    document.body.appendChild(test_div)

    //need a hashtag to get this element in this function
    let button = document.querySelector('#getter')
    button.addEventListener('click', (e) => {
        console.log("Button Clicked")
        // works up until here
        let div = document.createElement('div')
        div.setAttribute('id', 'contact_form')
        div.innerHTML = "<h1>The button-click div is working<h1>"
        document.body.appendChild(div)

        let form = document.createElement('form')
        //div.appendChild(form)
        form.setAttribute('action', "register.php")
        form.setAttribute('method', "post")
        div.appendChild(form)
        let email = document.createElement('input')
        email.setAttribute('type', "email")
        email.setAttribute('name', "Email Address")
        email.setAttribute('id', "email")
        form.appendChild(email)
        let submit = document.createElement('input')
        submit.setAttribute('type', "submit")
        submit.setAttribute('value', "Submit your email address")
        submit.setAttribute('id', 'submitButton')
        form.appendChild(submit)

    })


})






