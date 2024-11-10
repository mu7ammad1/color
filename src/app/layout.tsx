import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";
import Navbar from "@/components/Navbar";
import { Left, Right } from "@/components/Menus";
import PalettesProvider from "@/components/UsernameContext";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

export const metadata: Metadata = {
  title: {
    template: "%s - Color Hunt",
    default: "Color Hunt - Color Palettes for Designers and Artists",
  },
  description:
    "افضل خطوط عربية و انجليزية تحميل و تجربة خطوط العربية و الانجليزية الاتينية",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased w-full flex justify-center bg-transparent dark:bg-[#202020]`}
      >
        <main className="w-full flex max-w-screen-2xl flex-col px-5">
          <Navbar />
          <div className="line mt-1"></div>
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
