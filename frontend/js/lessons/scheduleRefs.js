let refs = {
  dateInput: null,
  container: null,
};

export function setScheduleRefs({ dateInput, container }) {
  refs.dateInput = dateInput;
  refs.container = container;
}

export function getScheduleRefs() {
  return refs;
}
