const fs = require('fs');

function countStudents(path) {
  let data;
  try {
    data = fs.readFileSync(path, 'utf8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

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

  const totalStudents = students.filter((student) => student.length === headers.length).length;
  console.log(`Number of students: ${totalStudents}`);

  for (const [field, firstnames] of Object.entries(fields)) {
    console.log(`Number of students in ${field}: ${firstnames.length}. List: ${firstnames.join(', ')}`);
  }
}

module.exports = countStudents;
