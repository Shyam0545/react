import apache from '../apache.json';

export type Person = {
  agent_id: string;
  call_id: string;
  call_start: string;
  call_end : string;
  call_outcome : string;
  call_status : string;
  company_id : string;
  department_id : string;
  duration : string;
  row_id : string;
  timestamp : string;
};

//random time today
const today = () => {
  const today = new Date();
  today.setHours(Math.floor(Math.random() * 24));
  today.setMinutes(Math.floor(Math.random() * 60));
  today.setSeconds(Math.floor(Math.random() * 60));
  return today;
};


// const apache1 = JSON.stringify(apache);
// const unquoted = apache1.replace(/"([^"]+)":/g, '$1:');
export const data = apache
