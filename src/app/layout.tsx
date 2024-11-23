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
  keywords: [
    "Color Hunt",
    "colors",
    "coolors",
    "ColorHunt.fun",
    "Colorful",
    "colors palette",
  ],
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

  // OpenGraph

  openGraph: {
    title: "Color Palettes for Designers and Artists",
    description:
      "Discover the newest hand-picked color palettes of Color Hunt. Get color inspiration for your design and art projects.",
    url: "https://colorhunt.fun",
    siteName: "colorhunt.fun",
    locale: "en_US",
    type: "website",
    images: [
      {
        url: "https://colorhunt.fun/backgound.png",
        width: 800,
        height: 600,
        alt: "My custom alt",
      },
      {
        url: "https://colorhunt.fun/backgound.png",
        width: 1800,
        height: 1600,
        alt: "My custom alt",
      },
    ],
  },
  category: "Colorful",

  // Icons

  icons: {
    icon: "/favicon.ico",
    shortcut: "/colorhunt.svg",
    apple: "/apple-touch-icon.png",
    other: {
      rel: "apple-touch-icon-precomposed",
      url: "/apple-touch-icon.png",
    },
  },

  // Twitter
  twitter: {
    card: "summary_large_image",
    title: "Color Palettes for Designers and Artists",
    description:
      "Discover the newest hand-picked color palettes of Color Hunt. Get color inspiration for your design and art projects.",
    siteId: "1467726470533754880",
    creator: "@colorhunt.fun",
    creatorId: "1467726470533754880",
    images: {
      url: "https://colorhunt.fun/backgound.png",
      alt: "colorhunt.fun Logo",
    },
  },

  verification: {
    google: "BeJRm1IT38d08QmUcE4b5WscOVe9qW9loDAzhWlyFgg",
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
