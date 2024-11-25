/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import { Button } from "@/components/ui/button";
import Link from "next/link";
import React from "react";

export default function DownloadButton({
  color1,
  color2,
  color3,
  color4,
}: {
  color1: string;
  color2: string;
  color3: string;
  color4: string;
}) {
  const handleDownload = (e: React.MouseEvent<HTMLAnchorElement>) => {
    e.preventDefault(); // منع السلوك الافتراضي للرابط
    const url = `/og/${color1 + color2 + color3 + color4}.png`;
    const link = document.createElement("a");
    link.href = url;
    link.download = `palette-${color1}-${color2}-${color3}-${color4}.png`;
    link.click();
  };

  return (
    <Link
      href={`/palette/${color1 + color2 + color3 + color4}`}
      onMouseDown={handleDownload} // يستخدم onMouseDown لمعالجة التنزيل
    >
      <Button variant={"outline"} size={"default"}>
        Image
      </Button>
    </Link>
  );
}
