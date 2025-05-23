process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.on('data', (data) => {
  const input = data.toString().trim();
  if (input.length > 0) {
    console.log(`Your name is: ${input}`);
  }
});

process.stdin.on('end', () => {
  console.log('This important software is now closing');
});
