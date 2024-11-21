/* eslint-disable @typescript-eslint/no-unused-vars */
import Home from "../page";

export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {

  return <Home />;
}
