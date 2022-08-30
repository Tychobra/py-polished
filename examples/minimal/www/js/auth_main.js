const auth_main = (ns_prefix) => {

  let cookie_options = {}
  if (location.protocol === 'https:') {
    // add cookie options that browsers are starting to require to allow you to
    // use cookies within iframes. Only works when app is running on https.
    cookie_options.sameSite = 'none'
    cookie_options.secure = true
  }

  const sign_in = (email, password) => {

    const polished_cookie = "p" + Math.random()

    Cookies.set(
      'polished',
      polished_cookie,
      cookie_options
    )

    Shiny.setInputValue(`${ns_prefix}check_jwt`, {
      email: email,
      password: password,
      cookie: polished_cookie
    }, {
      event: "priority"
    });
  }

  $(document).on("click", `#${ns_prefix}register_submit`, () => {
    const email = $(`#${ns_prefix}register_email`).val().toLowerCase()
    const password = $(`#${ns_prefix}register_password`).val()
    const password_2 = $(`#${ns_prefix}register_password_verify`).val()

    if (password !== password_2) {
      // Event to reset Register loading button from loading state back to ready state
      loadingButtons.resetLoading(`${ns_prefix}register_submit`);

      toastr.error("The passwords do not match", null, toast_options)
      console.log("the passwords do not match")

      return
    } else if (password == "" && password_2 == "") {
      // Event to reset Register loading button from loading state back to ready state
      loadingButtons.resetLoading(`${ns_prefix}register_submit`);

      toastr.error("Invalid password", null, toast_options)
      console.log("invalid password")

      return
    }



    const polished_cookie = "p" + Math.random()

    Cookies.set(
      'polished',
      polished_cookie,
      { expires: cookie_expires }
    )

    Shiny.setInputValue(`${ns_prefix}register_js`, {
      email: email,
      password: password,
      cookie: polished_cookie
    }, {
      event: "priority"
    });

  })




  $(document).on("click", `#${ns_prefix}sign_in_submit`, () => {

    const email = $(`#${ns_prefix}sign_in_email`).val().toLowerCase()
    const password = $(`#${ns_prefix}sign_in_password`).val()

    sign_in(email, password)

  })


  Shiny.addCustomMessageHandler(
    "shiny_reload",
    function(message) {
      debugger
      location.reload()
    }
  )

}