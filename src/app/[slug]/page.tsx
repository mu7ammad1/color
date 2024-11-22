import React from "react";

export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  // Resolve params if needed
  const { slug } = await params;

  return (
    <div className={`uppercase`}>
      HELLO WORLD : <br />
      <span style={{ color: "red" }}>{slug.toUpperCase()}</span>
    </div>
  );
}
