const express = require('express');
const fs = require('fs').promises;

const database = process.argv[2];

function countStudents(path) {
  return fs.readFile(path, 'utf8')
    .then((data) => {
      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const headers = lines[0].split(',');

      const fieldIdx = headers.indexOf('field');
      const firstnameIdx = headers.indexOf('firstname');

      const students = lines.slice(1).map((line) => line.split(','));
      const fields = {};

      students.forEach((student) => {
        if (student.length < headers.length) return;
        const field = student[fieldIdx];
        const firstname = student[firstnameIdx];
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });

      const totalStudents = students.filter(
        (student) => student.length === headers.length,
      ).length;

      let result = `Number of students: ${totalStudents}\n`;
      for (const [field, firstnames] of Object.entries(fields)) {
        result += `Number of students in ${field}: ${firstnames.length}. List: ${firstnames.join(', ')}\n`;
      }
      return result.trim();
    });
}

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.set('Content-Type', 'text/plain');
  try {
    const result = await countStudents(database);
    res.send(`This is the list of our students\n${result}`);
  } catch (err) {
    res.status(500).send('Cannot load the database');
  }
});

app.listen(1245);

module.exports = app;
