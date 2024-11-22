import type { Metadata } from "next";
import "./globals.css";
import Navbar from "@/components/Navbar";
import { Left, Right } from "@/components/Menus";
import PalettesProvider from "@/components/UsernameContext";

export const metadata: Metadata = {
  title: {
    template: "%s - Color Hunt",
    default: "Color Palettes for Designers and Artists",
  },
  description:
    "Discover the newest hand-picked color palettes of Color Hunt. Get color inspiration for your design and art projects.",
  generator: "ColorHunt.fun",
  applicationName: "ColorHunt.fun",
  referrer: "origin-when-cross-origin",
  keywords: ["Color Hunt", "colors", "coolors", "ColorHunt.fun"],
  authors: [
    { name: "Hasub", url: "hasub.co" },
    { name: "mu7ammad", url: "https://www.instagram.com/mu7amm.ad" },
  ],
  creator: "Mu7ammad osama",
  publisher: "hasub",
  formatDetection: {
    email: false,
    address: false,
    telephone: false,
  },
  metadataBase: new URL("https://colorhunt.fun"),
  robots: {
    index: true,
    follow: true,
    nocache: false,
    googleBot: {
      index: true,
      follow: true,
      noimageindex: false,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
  twitter: {
    card: "summary_large_image",
    title: "Color Palettes for Designers and Artists",
    description:
      "Discover the newest hand-picked color palettes of Color Hunt. Get color inspiration for your design and art projects.",
    siteId: "1467726470533754880",
    creator: "@colorhunt.co",
    creatorId: "1467726470533754880",
    images: ["https://nextjs.org/og.png"], // Must be an absolute URL
  },
  verification: {
    google: "G-01Z3VZQFP9",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`antialiased w-full flex justify-center bg-transparent dark:bg-[#202020]`}
      >
        <main className="w-full flex max-w-screen-2xl flex-col px-5 max-md:px-0">
          <Navbar />
          <section className="flex w-full h-full *:w-full py-5">
            <PalettesProvider>
              <Right />
              <section className="px-3">{children}</section>
              <Left />
            </PalettesProvider>
          </section>
        </main>
      </body>
    </html>
  );
}
