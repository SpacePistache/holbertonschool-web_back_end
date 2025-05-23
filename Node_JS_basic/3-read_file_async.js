const fs = require('fs').promises;

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
      console.log(`Number of students: ${totalStudents}`);

      for (const [field, firstnames] of Object.entries(fields)) {
        console.log(`Number of students in ${field}: ${firstnames.length}. List: ${firstnames.join(', ')}`);
      }
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
