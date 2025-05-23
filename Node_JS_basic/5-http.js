const http = require('http');
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

const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    if (!database) {
      res.statusCode = 500;
      res.end('Database filename was not provided');
      return;
    }
    res.statusCode = 200;
    res.write('This is the list of our students\n');
    countStudents(database)
      .then((data) => {
        res.end(data);
      })
      .catch(() => {
        res.statusCode = 500;
        res.end('Cannot load the database');
      });
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245);

module.exports = app;
