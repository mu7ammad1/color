/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { usePathname } from "next/navigation";
import Link from "next/link";
import { usePalettes } from "./UsernameContext";
import { X } from "lucide-react";

export function Left() {
  const { palettes, deletePalette, errorMessage } = usePalettes();

  return (
    <div className="flex flex-col w-full max-w-80 pl-5 h-screen sticky top-20 overflow-y-scroll rounded-md border-none p-0 max-[900px]:hidden">
      <div className="my-3">
        <h3 className="scroll-m-10 text-xl font-medium tracking-tight">
          Color Palettes for Designers and Artists
        </h3>
        <p className="leading-7 [&:not(:first-child)]:my-3">
          Discover the newest hand-picked palettes of Color Hunt
        </p>
        <div className="line w-full"></div>
      </div>
      <div className="flex w-full">
        <Link href={`/collection`} className="text-lg font-medium mb-4">
          My Collection
        </Link>
      </div>
      {errorMessage && <p className="text-red-500">{errorMessage}</p>}

      <div
        className={`w-full grid grid-cols-3 gap-3`}
        key={Date.now().toString()}
      >
        {palettes.map((palette) => (
          <div key={palette.id + Date.now().toString()}>
            <div
              className="w-full h-7 rounded-tl-xl rounded-tr-xl p-[2px]"
              style={{ backgroundColor: `#${palette.color1}` }}
            >
              <button
                onClick={() => deletePalette(palette.id)}
                className={`bg-stone-50 p-[2px] rounded-full`}
              >
                <X className={`size-4`} />
              </button>
            </div>
            <div
              className="w-full h-7"
              style={{ backgroundColor: `#${palette.color2}` }}
            ></div>
            <div
              className="w-full h-7"
              style={{ backgroundColor: `#${palette.color3}` }}
            ></div>
            <div
              className="w-full h-7 rounded-bl-xl rounded-br-xl"
              style={{ backgroundColor: `#${palette.color4}` }}
            ></div>
          </div>
        ))}
      </div>
    </div>
  );
}

export function Right() {
  const Pathname = usePathname();

  return (
    <section className="flex flex-col w-full max-w-48 pr-5 h-screen sticky top-20 overflow-y-scroll rounded-md border-none p-0">
      <div className="w-full flex flex-col gap-1">
        <Link
          href={`/`}
          className={`p-3 flex gap-3 rounded-xl items-center  ${
            Pathname === `/` ? `bg-stone-100` : `hover:bg-stone-50`
          }`}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill={Pathname === `/` ? `currentColor` : `none`}
            viewBox="0 0 24 24"
            strokeWidth={1}
            stroke="currentColor"
            className="size-6"
          >
            <path d="M9.937 15.5A2 2 0 0 0 8.5 14.063l-6.135-1.582a.5.5 0 0 1 0-.962L8.5 9.936A2 2 0 0 0 9.937 8.5l1.582-6.135a.5.5 0 0 1 .963 0L14.063 8.5A2 2 0 0 0 15.5 9.937l6.135 1.581a.5.5 0 0 1 0 .964L15.5 14.063a2 2 0 0 0-1.437 1.437l-1.582 6.135a.5.5 0 0 1-.963 0z" />
            <path d="M20 3v4" />
            <path d="M22 5h-4" />
            <path d="M4 17v2" />
            <path d="M5 18H3" />
          </svg>
          <p className="text-lg font-thin hue-rotate-180">New</p>
        </Link>
        <Link
          href={`/popular`}
          className={`p-3 flex gap-3 rounded-xl items-center  ${
            Pathname === `/popular` ? `bg-stone-100` : `hover:bg-stone-50`
          }`}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill={Pathname === `/popular` ? `currentColor` : `none`}
            viewBox="0 0 24 24"
            strokeWidth={1}
            stroke="currentColor"
            className="size-6"
          >
            <path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z" />
          </svg>
          <p className="text-lg font-thin">Popular</p>
        </Link>
        <Link
          href={`/random`}
          className={`p-3 flex gap-3 rounded-xl items-center  ${
            Pathname === `/random` ? `bg-stone-100` : `hover:bg-stone-50`
          }`}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill={Pathname === `/random` ? `currentColor` : `none`}
            viewBox="0 0 24 24"
            strokeWidth={1}
            stroke="currentColor"
            className="size-6"
          >
            <rect width="12" height="12" x="2" y="10" rx="2" ry="2" />
            <path d="m17.92 14 3.5-3.5a2.24 2.24 0 0 0 0-3l-5-4.92a2.24 2.24 0 0 0-3 0L10 6" />
            <path d="M6 18h.01" />
            <path d="M10 14h.01" />
            <path d="M15 6h.01" />
            <path d="M18 9h.01" />
          </svg>
          <p className="text-lg font-thin">Random</p>
        </Link>
        <Link
          href={`/collection`}
          className={`p-3 flex gap-3 rounded-xl items-center  ${
            Pathname === `/collection` ? `bg-stone-100` : `hover:bg-stone-50`
          }`}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill={Pathname === `/collection` ? `currentColor` : `none`}
            viewBox="0 0 24 24"
            strokeWidth={1}
            stroke="currentColor"
            className="size-6"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z"
            />
          </svg>
          <p className="text-lg font-thin">Collection</p>
        </Link>
        <div className="line my-2"></div>
        {Links(Pathname, `retro`)}
        {Links(Pathname, `vintage`)}
        {Links(Pathname, `cool`)}
        {Links(Pathname, `classic`)}
        {Links(Pathname, `yellow`)}
        {Links(Pathname, `beige`)}
        {Links(Pathname, `black`)}
        {Links(Pathname, `sky`)}
        {Links(Pathname, `vintage`)}
        {Links(Pathname, `teal`)}
        {Links(Pathname, `maroon`)}
        {Links(Pathname, `yellow`)}
        {Links(Pathname, `beige`)}
        {Links(Pathname, `black`)}
        {Links(Pathname, `sky`)}
        {Links(Pathname, `vintage`)}
        {Links(Pathname, `teal`)}
        {Links(Pathname, `maroon`)}
        {Links(Pathname, `yellow`)}
        {Links(Pathname, `beige`)}
        {Links(Pathname, `black`)}
        {Links(Pathname, `sky`)}
        {Links(Pathname, `vintage`)}
        {Links(Pathname, `teal`)}
        {Links(Pathname, `maroon`)}
        {Links(Pathname, `yellow`)}
        {Links(Pathname, `beige`)}
        {Links(Pathname, `black`)}
        {Links(Pathname, `sky`)}
        {Links(Pathname, `vintage`)}
        {Links(Pathname, `teal`)}
        {Links(Pathname, `maroon`)}
        {Links(Pathname, `yellow`)}
        {Links(Pathname, `beige`)}
        {Links(Pathname, `black`)}
        {Links(Pathname, `sky`)}
        {Links(Pathname, `vintage`)}
        {Links(Pathname, `teal`)}
        {Links(Pathname, `maroon`)}
        {Links(Pathname, `yellow`)}
        {Links(Pathname, `beige`)}
        {Links(Pathname, `black`)}
      </div>
    </section>
  );
}
function Links(Pathname: string, href: string) {
  return (
    <Link
      href={`/palettes/${href}`}
      className={`p-2 px-4 flex gap-3 rounded-full items-center  ${
        Pathname === `/palettes/${href}` ? `bg-stone-100` : `hover:bg-stone-50`
      }`}
    >
      <p className="text-xs font-thin capitalize">{href}</p>
    </Link>
  );
}
