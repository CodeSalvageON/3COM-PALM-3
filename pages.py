html1 = """
<!DOCTYPE html>
<html>
  <head>
    <link href="https://codesalvageon.github.io/magichat/styles/index.css" rel="stylesheet" type="text/css">

    <meta content="Embed Title" property="og:title" />
    <meta content="Site Description" property="og:description" />
    <meta content="https://embed.com/this-is-the-site-url" property="og:url" />
    <meta content="https://embed.com/embedimage.png" property="og:image" />
    <meta content="#43B581" data-react-helmet="true" name="theme-color" />

    <style>
@font-face {
  font-family: Commodore;
  src: url('https://codesalvageon.github.io/magichat/fonts/FSEX300.ttf');
}

body {
  font-family: Commodore;
  background-color: black;
}

#window {
  width: 400px;
  height: 400px;
  background-color: #99fa96;
  margin: auto;
  position: absolute;
  box-shadow: 2px 2px 5px #99fa96;
  top: 0; left: 0; bottom: 0; right: 0;
}
    </style>
    <link href="https://codesalvageon.github.io/magichat/styles/3com.css" rel="stylesheet" type="text/css">
  </head>
  <body class="crt">
    <section id="window" class="add-scroll">
      <img src="https://codesalvageon.github.io/magichat/images/Screen%20Shot%202022-02-27%20at%2010.17.22%20PM.png" id="welcome" width="400" height="400">
      <section id="mail1" class="absolute-center">
        <p>Connect to Electronic Mail</p>
        <i>This account only lasts while you're here...so don't waste it!</i>
        <hr/>
        <form id="creation-form">
          <p>Set Electronic Mail Handle: <input type="text" id="mail-handle1" required></p>
          <p>Set Profile Photo URL: <input type="text" id="pfp-url" placeholder="Not required"></p>
          <button>Connect</button>
        </form>
        <hr/>
        <p id="display-email"></p>
        <p><img src='' width="150" height="150" id="display-pfp"></p>
      </section>
      <section id="mail2" class="absolute-center">
      <p>Mail!</p>
      <hr/>
      <section id="feed">
      </section>
      </section>
    </section>

    <script src="https://codesalvageon.github.io/magichat/scripts/jquery.js"></script>
    <script src="https://codesalvageon.github.io/magichat/scripts/3com.js"></script>
  </body>
</html>
"""