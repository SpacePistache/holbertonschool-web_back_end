import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((results) => results.map((result) => {
    let value;

    if (result.status === 'fulfilled') {
      value = result.value;
    } else {
      value = result.reason;
    }

    return {
      status: result.status,
      value,
    };
  }));
}
