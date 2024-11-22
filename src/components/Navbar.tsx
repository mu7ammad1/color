import { Instagram, Search } from "lucide-react";
import { Button } from "./ui/button";
import Link from "next/link";
import Image from "next/image";
import favicon from "@/app/photos/image.png";
import { Input } from "@/components/ui/input";

export default function Navbar() {
  return (
    <nav className="flex flex-col w-full sticky top-0 z-50 bg-background px-2">
      <section className={`w-full flex justify-between items-center`}>
        <Link
          href={`/`}
          className={`w-full max-w-max max-sm:max-w-fit flex gap-3 items-center justify-start`}
        >
          <Image src={favicon} alt="alten" className="w-14" />
          <p className={`font-medium text-xl max-sm:hidden`}>Color hunt</p>
        </Link>
        <div className="w-full flex justify-center items-center p-0">
          <div className="w-[90%] m-0 px-2 pr-5 flex gap-2 justify-center items-center border-[1px] focus-within:border-[1px] focus-within:border-offset-2 nsus rounded-full">
            <Search />
            <Input
              className={`w-full focus-visible:ring-0 focus-visible:ring-offset-0 shadow-none border-none p-0 m-0 nsus`}
            />
          </div>
        </div>
        <div className="w-full max-w-fit flex gap-3 justify-end items-center">
          <Button
            variant={"secondary"}
            size={"icon"}
            className="rounded-full *:dark:fill-white max-md:hidden"
            aria-label="Cofee me"
          >
            <svg
              viewBox="0 0 512 512"
              xmlns="http://www.w3.org/2000/svg"
              fillRule="evenodd"
              clipRule="evenodd"
              strokeLinejoin="round"
              strokeMiterlimit="2"
            >
              <g transform="matrix(.47407 0 0 .47407 .383 .422)">
                <clipPath id="prefix__a">
                  <path d="M0 0h1080v1080H0z" />
                </clipPath>
                <g clipPath="url(#prefix__a)">
                  <path
                    d="M1033.05 324.45c-.19-137.9-107.59-250.92-233.6-291.7-156.48-50.64-362.86-43.3-512.28 27.2-181.1 85.46-237.99 272.66-240.11 459.36-1.74 153.5 13.58 557.79 241.62 560.67 169.44 2.15 194.67-216.18 273.07-321.33 55.78-74.81 127.6-95.94 216.01-117.82 151.95-37.61 255.51-157.53 255.29-316.38z"
                    fillRule="nonzero"
                  />
                </g>
              </g>
            </svg>
          </Button>
          <Button
            variant={"secondary"}
            size={"icon"}
            className="rounded-full max-md:hidden"
            aria-label="Instagram icon"
          >
            <Instagram />
          </Button>
          <Button
            variant={"secondary"}
            size={"icon"}
            className="rounded-full"
            aria-label="Instagram icon"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill={`currentColor`}
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
          </Button>
        </div>
      </section>
      <div className="w-full line"></div>
    </nav>
  );
}
