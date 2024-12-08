/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './planner/templates/planner/**/*.html',
    './**/*.py',
  ],
  theme: {
    extend: {},
  },
  plugins: [require('daisyui')],
};

