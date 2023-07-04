API_URL = "http://localhost:5000";

const handleClickNmap = async () => {
  console.log("nmap");
  const c = await axios.get(API_URL + "/nmap");
  console.table(c);
};

const handleClickWireshark = async () => {
  console.log("wireshark");
  const c = await axios.get(API_URL + "/wireshark");
  console.table(c);
};
