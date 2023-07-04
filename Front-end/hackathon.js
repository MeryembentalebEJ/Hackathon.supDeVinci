API_URL = "http://localhost:5000";

const handleClickNmap = async () => {
  console.log("nmap");
  const response = await axios.get(API_URL + "/nmap");
  console.table(response);
};

const handleClickWireshark = async () => {
  console.log("wireshark");
  const response = await axios.get(API_URL + "/wireshark");
  console.table(response);
};
