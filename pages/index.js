import Head from "next/head";
import Link from "next/link";
import { useState } from "react";
import { useRouter } from "next/router";
import { getStates } from "../lib/api";
import { humanize } from "../lib/utils";
import Tabs from "../components/Tabs";
import "@fortawesome/fontawesome-svg-core/styles.css";
import {
  faLungsVirus,
  faSyringe,
  faHospital,
  faPhoneAlt,
  faAmbulance,
  faCapsules,
} from "@fortawesome/free-solid-svg-icons";
import Selector from "../components/Selector";

const tabsInfo = [
  { name: "Oxygen", icon: faLungsVirus, link: "/" },
  { name: "Medicine", icon: faCapsules, link: "/medicines" },
  { name: "Hospital", icon: faHospital, link: "/hospitals" },
  { name: "Ambulance", icon: faAmbulance, link: "/ambulance" },
  { name: "Helpline", icon: faPhoneAlt, link: "/helpline" },
  { name: "Plasma", icon: faSyringe, link: "/plasma" },
];

export default function Home() {
  return (
    <div>
      <Head>
        <title>Life | Coronasafe network</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <section className="flex flex-col items-center md:pt-20">
        <h1 className="mt-4 font-black text-6xl text-gray-900">LIFE</h1>
        <h2 className="mt-4 font-semibold text-xl text-gray-900">
          Verified Crowd Sourced Emergency Services Directory
        </h2>
        <div className="mt-4 ">
          <Tabs tabsInfo={tabsInfo} />
        </div>
        <div className="w-full md:w-3/4 px-2">
          <Selector />
        </div>
        <div className="flex flex-wrap items-center justify-evenly mt-6 ">
          {getStates().map((s) => {
            return (
              <Link href={`[state]`} as={`${s}`}>
                <span className="p-2 text-sm md:text-md font-normal hover:font-bold cursor-pointer hover:text-gray-900 text-gray-500">
                  {humanize(s)}
                </span>
              </Link>
            );
          })}
        </div>
      </section>
    </div>
  );
}