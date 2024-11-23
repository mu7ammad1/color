import type { MetadataRoute } from "next";
import { getSITEMAPS } from "./actions/getAction";

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const Dataa = await getSITEMAPS();

  // Static entries
  const staticEntries: MetadataRoute.Sitemap = [
    {
      url: "https://colorhunt.fun",
      lastModified: "2021-01-01",
      changeFrequency: "weekly",
      priority: 1,
    },
    {
      url: "https://colorhunt.fun/collection",
      lastModified: "2021-01-01",
      changeFrequency: "weekly",
      priority: 0.7,
    },
    {
      url: "https://colorhunt.fun/palette",
      lastModified: "2021-01-01",
      changeFrequency: "weekly",
      priority: 0.7,
    },
    {
      url: "https://colorhunt.fun/popular",
      lastModified: "2021-01-01",
      changeFrequency: "weekly",
      priority: 0.7,
    },
    {
      url: "https://colorhunt.fun/random",
      lastModified: "2021-01-01",
      changeFrequency: "weekly",
      priority: 0.7,
    },
  ];

  // Dynamic entries
  const dynamicEntries: MetadataRoute.Sitemap =
    Dataa?.map((item) => ({
      url: `https://colorhunt.fun/palette/${item.id}`,
      lastModified: item.lastModified || `2021-01-01`,
      changeFrequency: "weekly",
      priority: 0.5,
      images: [`https://colorhunt.fun/og/${item.id}.png`], // Dynamic image URL
    })) || [];

  // Combine static and dynamic entries
  return [...staticEntries, ...dynamicEntries];
}
