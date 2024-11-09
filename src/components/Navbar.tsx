import { Facebook, Instagram } from "lucide-react";
import { Button } from "./ui/button";
import Link from "next/link";
import Image from "next/image";
import favicon from "@/app/photos/image.png";

export default function Navbar() {
  return (
    <nav className={`w-full flex justify-between items-center`}>
      <Link href={`/`} className={`w-full max-w-52 flex gap-3 items-center justify-center`}>
        <Image src={favicon} alt="alten" className="w-14" />
        <p className={`font-medium text-xl`}>Color hunt</p>
      </Link>
      <div className="w-full flex gap-2 justify-center items-center">
        <Button
          variant={"secondary"}
          size={"icon"}
          className="rounded-full"
          aria-label="Instagram icon"
        >
          <Instagram />
        </Button>
      </div>
      <div className="w-full max-w-80 flex gap-2 justify-center items-center">
        <Button
          variant={"secondary"}
          size={"icon"}
          className="rounded-full *:dark:fill-white"
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
          className="rounded-full *:dark:fill-white"
          aria-label="Facebook icon"
        >
          <Facebook className="fill-stone-800" />
        </Button>
        <Button
          variant={"secondary"}
          size={"icon"}
          className="rounded-full"
          aria-label="Instagram icon"
        >
          <Instagram />
        </Button>
      </div>
    </nav>
  );
}
