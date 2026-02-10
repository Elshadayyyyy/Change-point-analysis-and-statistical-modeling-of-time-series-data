import { useEffect, useState } from "react";
import axios from "axios";
import PriceChart from "./PriceChart";
import EventsTable from "./EventsTable";
import "./App.css";

function App() {
  const [prices, setPrices] = useState([]);
  const [events, setEvents] = useState([]);
  const [changePoints, setChangePoints] = useState([]);
  useEffect(() => {
    axios.get("http://127.0.0.1:5000/prices").then((res) => {
      setPrices(res.data);
    });
    axios.get("http://127.0.0.1:5000/events").then((res) => {
      setEvents(res.data);
    });
    axios.get("http://127.0.0.1:5000/change_points").then((res) => {
      setChangePoints(res.data);
    });
  }, []);
 return (
    <div className="App">
      <h1>Brent Oil Price Dashboard</h1>
      <PriceChart data={prices} changePoints={changePoints} />
      <EventsTable events={events} />
    </div>
  );
}
export default App;
