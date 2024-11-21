"use client";
/* eslint-disable @typescript-eslint/no-explicit-any */
import React, { useState } from "react";

function FuncopyToClipboard(text: string) {
  navigator.clipboard.writeText(text).catch((err) => {
    console.error("فشل النسخ:", err);
  });
}

export function CopyToClipboardHex({ color }: any) {
  const [isCopied, setIsCopied] = useState(false);

  const handleCopy = () => {
    FuncopyToClipboard(color);
    setIsCopied(true);
    setTimeout(() => setIsCopied(false), 1000); // إخفاء الرسالة بعد ثانية واحدة
  };

  return (
    <span
      onClick={handleCopy}
      className="text-sm hover:bg-neutral-100 px-2 py-1 rounded-xl duration-300 cursor-pointer"
    >
      {isCopied ? "copied" : color}
    </span>
  );
}

export function CopyToClipboardLink({ link, display }: any) {
  const [isCopied, setIsCopied] = useState(false);

  const handleCopy = () => {
    FuncopyToClipboard(link);
    setIsCopied(true);
    setTimeout(() => setIsCopied(false), 1000); // إخفاء الرسالة بعد ثانية واحدة
  };

  return (
    <span
      onClick={handleCopy}
      className="text-sm hover:bg-neutral-100 px-2 py-1 rounded-xl duration-300 cursor-pointer"
    >
      {isCopied ? "copied" : display}
    </span>
  );
}
