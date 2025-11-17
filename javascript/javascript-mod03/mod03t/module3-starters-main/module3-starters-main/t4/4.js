'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];

document.addEventListener('DOMContentLoaded', () => {
    const target = document.getElementById('target'); // this is a <select>

    // The students array — each object has id and name
    const students = [
        { id: '2345768', name: 'John' },
        { id: '2134657', name: 'Paul' },
        { id: '5423679', name: 'Jones' }
    ];

    // Loop through the students array
    for (let i = 0; i < students.length; i++) {
        // Create a new <option> element
        const option = document.createElement('option');

        // Set the value attribute (student ID)
        option.value = students[i].id;

        // Set the displayed text (student name)
        option.textContent = students[i].name;

        // Append the option to the <select id="target">
        target.appendChild(option);
    }
});