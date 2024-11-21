import Home from "../page";

export default async function Page({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const slug = (await params).slug;

  return (
    <section>
      <Home />
    </section>
  );
}
