import React from "react";
import PriceChart from "./PriceChart";
import EventsTable from "./EventsTable";

export default function Dashboard() {
  return (
    <div>
      <h1>Brent Oil Prices Dashboard</h1>
      <PriceChart />
      <EventsTable />
    </div>
  );
}
