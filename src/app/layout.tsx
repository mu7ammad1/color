import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";
import Navbar from "@/components/Navbar";
import { Left, Right } from "@/components/Menus";

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
    template: "%s | الخطوط",
    default: "alkhutut | الخطوط",
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
        className={`${geistSans.variable} ${geistMono.variable} antialiased w-full flex justify-center bg-transparent dark:bg-[#202020] box-border`}
      >
        <main className="w-full flex max-w-screen-xl flex-col px-5">
          <Navbar />
          <section className="flex w-full h-full *:w-full">
            <Right />
            {children}
            <Left />
          </section>
        </main>
      </body>
    </html>
  );
}
