/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../templates/*/**.html",
    "../apps/iot/forms.py"
  ],
  theme: {
    extend: {},
    fontFamily: {
      "exo": ['"exo 2"'],
      "rale": ['"Raleway"'],
    },
  },
  plugins: [],
}

