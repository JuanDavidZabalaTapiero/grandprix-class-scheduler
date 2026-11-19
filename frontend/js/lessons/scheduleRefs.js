var refs = {
  dateInput: null,
  container: null,
  availabilityByDay: {},
};

export function setScheduleRefs({
  dateInput,
  container,
  availabilityByDay = {},
}) {
  refs.dateInput = dateInput;
  refs.container = container;
  refs.availabilityByDay = availabilityByDay;
}

export function getScheduleRefs() {
  return refs;
}
